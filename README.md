# PyMeUpCharlie

PyPoll and PyBank use python to read a csv file and create a script to analyze data and print it within terminal as well as exporting the analysis as a txt file.

## PyBank

First, the os and csv are both imported to allow us to read the csv file given, then using os.path.join we retrieve the file
Then, I set revch and mos as the lists to hold the revenue changes and month labels.
I also set certain variables to zero in order to start the values for the for loop in the next step.
Next, I used with open to open the csv file in the script and used next to skip the headerline in the file.
Then, I set the total revenue and row counts to zero for the for loop.
The for loop I made summed up the revenues in the 2nd column (row[1]), added the number of rows, and an if statement determined the change in revenues, then reset the previous month's revenue to the next month.
after that, calculations were made for the sum, average, max and min, and then used the mos list made earlier to index the month name to the corresponding max and min revenue changes.
Then, I printed all of the results, and then output a txt file using os.path.join.
The ouptut file was misnamed upon committing as OutputPyPoll.txt but it is for the PyBank portion.

## PyPoll

The setup for the first part is the same: importing the os and csv, locating and opening the file, then reading the file into the script and skipping the header.
Then, I set row count and winning votes to 0, creating dictionaries for votes and percentage of votes, and setting the candidate and winning candidate variables to nothing, so during the loop those names are filled in.
Then I started the for loop to count the number of rows(votes), and set the candidate name to the value in row[2].
I added an if statement to count the amount of votes for each candidate and add one everytime their names popped up.
I then made another for loop that put the amount of votes in the percentage dictionary by dividing by the row count, and added an if statement that compared the votes to the current holder of most votes and changed the winning candidate accordingly. 
Then, I printed all of the results, and then output a txt file using os.path.join. 
