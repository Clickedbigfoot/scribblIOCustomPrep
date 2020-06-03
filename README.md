# scribbl.io Custom List Preparer

This is a python script that take in lists of custom words and gets rid of duplicates and unnecessary spaces. This is intended so that you and friends could make lists individually and paste them into a single text document where they will be prepared for the scribbl.io game.

## Requirements

Must have python3 to run

## Usage

In the same directory, there must be a text file named "scribbleIO.txt". In this file, please type or paste your list of words with the words separated by commas. Then run 


```bash
python3 scribblIO.py
```

Afterwards, it prints the final formatted list to a new text file named "scribblIO_unique.txt". There will be no spaces next to commas, no duplicated words, no apostrophes (Words with apostrophes are not recognized as answers), and no uppercase words.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)