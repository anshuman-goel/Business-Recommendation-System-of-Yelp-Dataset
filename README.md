# Yelp
ADBI Captone Project

The authors contributed in building this project are:

- Anshuman Goel (agoel5@ncsu.edu)
- Siddharth Heggadahalli (ssheggad@ncsu.edu)
- Huy Tu (hqtu@ncsu.edu)

The json has been converted into csv files using the sample code provided by the Yelp at https://github.com/Yelp/dataset-examples

The converted CSV can't be loaded into Github due to large size.

Currently, the repository contains three folders namely:
- Code: where all code resides.
- Documents: All the documents provided by the professor.
- Sample Data: The filtered data files and sample initial files. The file merged_BR3.csv is used as the data for the current project.

Code Folder Details:
- The ReadData_AG.py is used for reading csv files, merging data, reducing dimensionality of data and data modification like modifying the rating. After completing data pre-processing, the final dataframe is stored in file to avoid processing the code again and again. Take a look at the path folder of data file.
- Before running evaluate.pynb make sure Spark is working properly on your machine. One will require Jupyter Notebook to run it. From terminal invoke the command IPYTHON_OPTS="notebook" $SPARK_HOME/bin/pyspark. Using the run button, the code can be executed. The code firstly reads the data from the file merged_BR3.csv. Divide the data into training and testing set. Train the model and evalute them using RMSE.
