import pandas as pd


def main():
    df = pd.read_csv('example_output.csv')
    df = df[['ItemType', 'Quantity']]
    importedQuantities = [*df['Quantity']]
    print(importedQuantities)
    print(importedQuantities[0])
    for i in range(0, 24):
        importedQuantities[i] += CartItems[i][1]

    df['Quantity'] = importedQuantities
    df.to_csv('example_output.csv')


if __name__ == '__main__':
    main()
