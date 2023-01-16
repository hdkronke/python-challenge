# Import
import os
import csv

# __________PYPOLL__________
# Import resources
election_csv = os.path.join(".", "resources", "election_data.csv")
# Name some variables
total_votes = 0
candidate_list = []
candidate_dict = {}

# Open and read csv
with open(election_csv) as election_file:
    election_reader = csv.reader(election_file, delimiter=",")
    # Read the header row first
    election_header = next(election_reader)
    # Find total votes
    for row in election_reader:
        # Add to the total vote count
        total_votes = total_votes + 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        if candidate_name not in candidate_list:
            # Add the candidate name to the candidate list.
            candidate_list.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_dict[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_dict[candidate_name] += 1
    print("Election Results")
    print("----------------------------------------")
    print("Total Votes:", total_votes)
    print("----------------------------------------")

    # Find individual candidate votes
    print(candidate_list[0], ":",
          round(candidate_dict["Charles Casper Stockham"]*100/total_votes, 3),
          "%", "(", candidate_dict["Charles Casper Stockham"], ")")
    print(candidate_list[1], ":",
          round(candidate_dict["Diana DeGette"]*100/total_votes, 3),
          "%", "(", candidate_dict["Diana DeGette"], ")")
    print(candidate_list[2], ":",
          round(candidate_dict["Raymon Anthony Doane"]*100/total_votes, 3),
          "%", "(", candidate_dict["Raymon Anthony Doane"], ")")
    # Find a cleaner way to code the votes
    votes_a = candidate_dict["Charles Casper Stockham"]
    votes_b = candidate_dict["Diana DeGette"]
    votes_c = candidate_dict["Raymon Anthony Doane"]
    print("----------------------------------------")

    # Find the winner
    if votes_a > votes_b and votes_a > votes_c:
        print("Winner: Charles Casper Stockham")
    if votes_b > votes_a and votes_b > votes_c:
        print("Winner: Diana DeGette")
    if votes_c > votes_a and votes_c > votes_b:
        print("Winner: Raymon Anthony Doane")
    print("----------------------------------------")

    # Export to .txt
    output_path = os.path.join(".", "analysis", "results.txt")
    with open(output_path, 'a') as csvfile:
        # Initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=" ")
        # Export the results
        csvwriter.writerow(["Election Results"])
        csvwriter.writerow(["----------------------------------------"])
        csvwriter.writerow(["Total Votes:", total_votes])
        csvwriter.writerow(["----------------------------------------"])
        csvwriter.writerow([candidate_list[0], ":",
                            round(votes_a*100/total_votes, 3),
                            "%", "(", votes_a, ")"])
        csvwriter.writerow([candidate_list[1], ":",
                            round(votes_b*100/total_votes, 3),
                            "%", "(", votes_b, ")"])
        csvwriter.writerow([candidate_list[2], ":",
                            round(votes_c*100/total_votes, 3),
                            "%", "(", votes_c, ")"])
        csvwriter.writerow(["----------------------------------------"])
        if votes_a > votes_b and votes_a > votes_c:
            csvwriter.writerow(["Winner: Charles Casper Stockham"])
        if votes_b > votes_a and votes_b > votes_c:
            csvwriter.writerow(["Winner: Diana DeGette"])
        if votes_c > votes_a and votes_c > votes_b:
            csvwriter.writerow(["Winner: Raymon Anthony Doane"])
        csvwriter.writerow(["----------------------------------------"])
