import os
import csv
import json
import configargparse


def json2csv(json_fname, csv_fname, sent_max_len):
    with open(json_fname) as f:
        data = json.load(f)
    csv_data = []
    for line in data:
        sentence = line['ent1'] + ' ENT_1_END ' + line['ent2'] + ' ENT_2_END '
        sentence += line['ori_sentence']

        sentence = ' '.join(sentence.split()[:sent_max_len])

        csv_line = {
            'tgt': line['label'],
            'input': sentence,
            'show_inp': sentence,
            'ent1': line['ent1'],
            'ent2': line['ent2'],
            'id': line['id'],
        }
        csv_data += [csv_line]
    with open(csv_fname, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=csv_line.keys())
        writer.writeheader()
        writer.writerows(csv_data)
    print('[Info] Writing {} data to {}'.format(len(csv_data), csv_fname))


def get_args():
    parser = configargparse.ArgumentParser(
        description='Options for preprocessing')
    parser.add_argument('-sent_max_len', default=100, type=int,
                        help='the maximum number of words allowed in a sentence')
    parser.add_argument('-tokenize', action='store_false', default=True,
                        help='whether to tokenize the sentences')
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    data_dir = os.path.dirname(os.path.realpath(__file__))

    for typ in 'train valid test'.split():
        json_fname = os.path.join(data_dir, '{}.json'.format(typ))
        csv_fname = os.path.join(data_dir, '{}.csv'.format(typ))

        json2csv(json_fname, csv_fname, args.sent_max_len)


if __name__ == '__main__':
    main()
