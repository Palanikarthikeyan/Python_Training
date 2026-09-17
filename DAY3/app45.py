import json
import pprint


def get_config_list():
    """Return the initial network configuration list."""
    return [
        "Type=ethernet",
        "Interface=eth0",
        "Onboot=yes",
        "bootproto=static",
    ]


def build_config(config_list):
    """Convert a key=value list into a dictionary."""
    config_dict = {}
    for item in config_list:
        key, value = item.split("=", 1)
        config_dict[key] = value
    return config_dict


def display_config(config_dict):
    """Display the configuration dictionary."""
    pprint.pprint(config_dict)


def update_config(config_dict):
    """Apply configuration updates and return the updated dictionary."""
    config_dict["Interface"] = "eth1"
    config_dict["bootproto"] = "dhcp"
    config_dict["IP"] = "10.20.40.50"
    config_dict["subnet"] = 24
    return config_dict


def convert_to_json(config_dict):
    """Convert Python dictionary to JSON string."""
    json_obj = json.dumps(config_dict, indent=4)
    print("JSON Object is created")
    return json_obj


def main():
    config_list = get_config_list()
    config_dict = build_config(config_list)
    display_config(config_dict)

    updated_config = update_config(config_dict)
    print("\nUpdated dict details:-")
    display_config(updated_config)

    json_data = convert_to_json(updated_config)
    print(json_data)
    print("Exit from main code")


if __name__ == "__main__":
    main()