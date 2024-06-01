import re
import uuid

def find_and_replace_uuids(filename):
    # Define the regex pattern for UUIDs
    uuid_pattern = re.compile(r'\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b', re.IGNORECASE)

    with open(filename, 'r') as file:
        content = file.read()
    
    # Find all UUIDs in the file
    old_uuids = uuid_pattern.findall(content)
    num_uuids = len(old_uuids)
    
    # Generate new UUIDs
    new_uuids = [str(uuid.uuid4()) for _ in range(num_uuids)]
    
    # Replace old UUIDs with new UUIDs
    for old_uuid, new_uuid in zip(old_uuids, new_uuids):
        content = content.replace(old_uuid, new_uuid, 1)  # Replace only the first occurrence each time

    # Write the updated content back to the file
    with open(filename, 'w') as file:
        file.write(content)
    
    return num_uuids

# Example usage
filename = 'scenario.yaml'
num_uuids = find_and_replace_uuids(filename)

print(f"Found and replaced {num_uuids} UUIDs in the file.")
