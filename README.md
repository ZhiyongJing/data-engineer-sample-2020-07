### Use pure python and build in module to read txt files and combine into csv file
> 
  1. Please only check the only modified main.py file
  2. Use python main.py to get output.csv
  3. Check the output file under data/destination/ folder

### The scenario:
- You have a vendor that delivers 2 files (`SOURCEDATA.TXT`, `SOURCECOLUMNS.txt`) every day at 6AM UTC. These files will land in `data/source/` for processing. For this assessment, you are provided the files in the `data/source/` path as if they were already delivered from the vendor.
- One file contains the raw pipe-delimited data (`SOURCEDATA.TXT`) without a header row.
- The other file (`SOURCECOLUMNS.txt`) contains pipe delimited data with 2 columns:
  - The first column contains an integer which represents *__the order in which these columns should
be displayed when combined with the data__* in `SOURCEDATA.TXT`. (__1__ being the first column)
  - The second column contains name of the column.


### The problem:
- The data must be loaded to a desired destination as a single file.
- This data needs to be represented in a single `.csv` file with a column row that is displaying the columns in the correct order as specified in column #1 of `SOURCECOLUMNS.txt`.

