import csv

if __name__ == '__main__':
    # You should not modify this part.
    import argparse


    parser = argparse.ArgumentParser()
    parser.add_argument('--training',
                       default='training.csv',
                       help='input training data file name')
    parser.add_argument('--testing',
                        default='testing.csv',
                        help='input testing data file name')
    parser.add_argument('--output',
                        default='output.csv',
                        help='output file name')
    args = parser.parse_args()
    size = 0
    with open(args.testing, newline='') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            size += 1
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(size-1):
            writer.writerow([0])