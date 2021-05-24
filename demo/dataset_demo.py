from ml_platform_sdk.dataset.dataset_service import DatasetService

ak = 'AKLTOTk1NmEwOTYyZDQ2NGJmNTk5M2E1MWY4N2NmMzA4M2Q'
sk = 'TnpjNFlUTmtZalZoTkRSaU5HRXdNV0l4TjJOaU9UWXlZekUxTnpBeE1tUQ=='
region = 'cn-north-1'

if __name__ == '__main__':
    client = DatasetService()
    client.set_ak(ak)
    client.set_sk(sk)

    # List Datasets
    # print(client.list_datasets())

    # Get Dataset
    # print(client.get_dataset('d-20210524144453-tr6mp'))

    # Download Dataset
    # manifest = client.download_dataset('d-20210524144453-tr6mp', './')

    # Split Dataset
    client.split_dataset('./train_dataset', './test_dataset',
                         'd-20210524144453-tr6mp')
