# -*- encoding: utf -*-
import json
import argparse


def triple2csv(file, file_csv):
    print('[Info] Generating CSV from {} to {}'.format(file, file_csv))

    import csv

    with open(file) as f:
        data = json.load(f)
    csv_data = []
    for line in data:
        {
            "triples": "A.C._Milan\tchairman\tSilvio_Berlusconi",
            "target": "The Chairman of AGENT_1 is PATIENT_1 .",
            "target_txt": "The Chairman of A C Milan is Silvio Berlusconi .",
            "ner2ent": {
                "AGENT_1": "A.C._Milan",
                "PATIENT_1": "Silvio_Berlusconi"
            }
        }
        target = line['target']
        ner2ent = line['ner2ent']
        triples = line['triples'].split(';;\t')
        triples = [triple.split('\t') for triple in triples]

        target = [word if word not in ner2ent else ner2ent[word] for word in
                  target.split()]
        target = ' '.join(target)
        for subj, predi, obj in triples:
            sentence = subj + ' ENT_1_END ' + obj + ' ENT_2_END ' + target
            csv_data.append(
                {
                    'tgt': '_'.join(predi.split()),
                    'input': sentence,
                    'show_inp': sentence,
                })

    with open(file_csv, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=csv_data[0].keys())
        writer.writeheader()
        writer.writerows(csv_data)


def main():
    parser = argparse.ArgumentParser(description='prepare csv for training')
    parser.add_argument('-dataset', default='webnlg', type=str)
    args = parser.parse_args()

    file_templ = 'data/' + args.dataset + '/{}.json'
    typ_list = 'train valid test'.split()
    for typ in typ_list:
        file = file_templ.format(typ)
        file_csv = file.replace('.json', '.csv')
        triple2csv(file, file_csv)


if __name__ == "__main__":
    main()
