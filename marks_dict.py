# Initialize an empty dictionary to store subject names and marks
subject_marks_dict = {}

# Function to get subject name and marks from the user
def get_subject_marks():
    subject = input("Enter the subject name (or 'stop' to finish): ")

    # Check if the user wants to stop
    if subject.lower() == 'stop':
        return None, None

    # Get marks from the user
    marks = float(input("Enter the marks for {}: ".format(subject)))

    return subject, marks

# Main loop to continuously get subject names and marks from the user
while True:
    subject, marks = get_subject_marks()

    # Break the loop if the user entered 'stop'
    if subject is None:
        break

    # Add subject and marks to the dictionary
    subject_marks_dict[subject] = marks

# Print the final dictionary
print("Subject-wise marks:")
for subject, marks in subject_marks_dict.items():
    print("{}: {}".format(subject, marks))
