import uuid

# Generate a new UUID
new_uuid = uuid.uuid4()
print(f"Generated UUID: {new_uuid}")

# Convert a UUID to string and vice versa
uuid_str = str(new_uuid)
parsed_uuid = uuid.UUID(uuid_str)

print(f"UUID as String: {uuid_str} of length: {len(uuid_str)}")
print("Parsed UUID:", parsed_uuid)

# Check if two UUIDs are equal
another_uuid = uuid.uuid4()
print("Another UUID:", another_uuid)

if new_uuid == another_uuid:
    print("The two UUIDs are equal.")
else:
    print("The two UUIDs are not equal.")



# ===================== UUID BASED ON STRING PASSED ==========================================================


def generate_uuid_based_on_value(value):
    # Use a predefined namespace UUID (e.g., UUID for DNS)
    namespace = uuid.UUID('6ba7b810-9dad-11d1-80b4-00c04fd430c8')

    # Generate a UUID based on the passed value
    generated_uuid = uuid.uuid5(namespace, str(value))
    print(f"This is of type: {type(str(generated_uuid))}")

    return generated_uuid


# Example: Generate a UUID based on the value "example"
result_uuid = generate_uuid_based_on_value("example")
print("Generated UUID:", result_uuid)
