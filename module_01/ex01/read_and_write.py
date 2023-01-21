def csv_to_tsv():
    with open('ds.csv', 'r') as in_csv, open('ds.tsv', 'w') as out_tsv:
        out_tsv.write(in_csv.read().replace('","', '"\t"')
                      .replace(',false,', '\tfalse\t').replace(',true,', '\ttrue\t'))


if __name__ == '__main__':
    csv_to_tsv()
