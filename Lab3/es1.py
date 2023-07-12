from typing import List, Any

import numpy as np
import pandas as pd
from mlxtend import *
from mlxtend.frequent_patterns import *
import timeit


def list_of_list_of_items(retails: pd.DataFrame):
    groups = []
    grouped_retails = retails.groupby('InvoiceNo')['Description'].apply(list)
    for i in range(0, len(grouped_retails)):
        groups.append(grouped_retails[i])
        # print(groups[i])
    return groups, grouped_retails


def compute_pa_matrix(invoice_no: list, all_items: list, grouped_retails: pd.DataFrame):
    pa_matrix = np.zeros((len(invoice_nos), len(all_items)))
    for i in range(0, len(invoice_nos)):
        for j in range(0, len(all_items)):
            if all_items[j] in grouped_retails[i]:
                pa_matrix[i, j] = 1
            # print(f"{pa_matrix[i, j]} ", end='')
        # print("")
    return pa_matrix


if __name__ == '__main__':
    init_retails = pd.read_csv("retails.csv")
    retails = (init_retails[~init_retails['InvoiceNo'].str.contains('C', case=False)]).reset_index(drop=True)
    # print(retails.to_string())

    groups, grouped_retails = list_of_list_of_items(retails)
    all_items = list(retails['Description'].drop_duplicates())
    # print(all_items)
    invoice_nos = list(retails['InvoiceNo'].drop_duplicates())
    invoice_nos.sort()
    # print(invoice_nos)
    pa_matrix = compute_pa_matrix(invoice_nos, all_items, grouped_retails)
    df = pd.DataFrame(data=pa_matrix, columns=all_items)

    fi = fpgrowth(df, 0.02)
    print(f"Number of itemsets: {len(fi)}")
    print(fi.to_string() + "\n")
    ar = association_rules(fi, metric='confidence', min_threshold=0.85, support_only=False)
    print(f"Number of association rules: {len(ar)}")
    print(ar.to_string())

    ap = apriori(df, 0.02)
    print(f"Number of itemsets: {len(ap)}")
    print(ap.to_string() + "\n")
    ar1 = association_rules(ap, metric='confidence', min_threshold=0.85, support_only=False)
    print(f"Number of association rules: {len(ar1)}")
    print(ar1.to_string())

    time_fpg = timeit.timeit(lambda: fpgrowth(df, 0.02), number=1)
    print(f"time spent by fpgrowth algorithm: {time_fpg}")
    time_apr = timeit.timeit(lambda: apriori(df, 0.02), number=1)
    print(f"time spent by apriori algorithm: {time_apr}")
