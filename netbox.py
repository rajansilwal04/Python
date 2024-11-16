# Open the original file in read mode
with open(r'/Users/rajan.silwal/Desktop/netbox.txt', 'r') as infile:
    # Read the content of the file
    content = infile.read()

# Replace all whitespace with commas
new_content = ','.join(content.split())

# Open the new file in write mode
with open(r'/Users/rajan.silwal/Desktop/new_netbox.txt', 'w') as outfile:
    # Write the modified content to the new file
    outfile.write(new_content)

print("Whitespace has been replaced with commas and saved to new_netbox.txt.")
