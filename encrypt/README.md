# Space Station Data Encryption

This is a collection of Python scripts that handles encryption of data being used on the space station. 

## Installation

1. Clone this repository to your local machine.
2. Install the required packages by running `pip install -r requirements.txt`.
3. Run the scripts to encrypt your data.

## Usage

To encrypt a file, run the `encrypt.py` script and pass in the file path as an argument:

```
python encrypt.py path/to/file
```

To decrypt a file, run the `decrypt.py` script and pass in the file path as an argument:

```
python decrypt.py path/to/file
```

**Note:** The key used for encryption and decryption is generated automatically and stored in the `key.key` file. Make sure to keep this file secure as it is required to decrypt the data.

## Contributing

Contributions to this project are welcome. If you find a bug or have a feature request, please open an issue on this repository. If you would like to contribute code, please fork this repository and submit a pull request.