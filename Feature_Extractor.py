from Url_Features import *  # Ensure this imports all the necessary functions

# Takes URL, extracts features, and returns numerical features which will be input to the model
def extract_features(url):
    url_features = []

    # hostname length
    i = hostname_length(url)
    url_features.append(i)

    # path length
    i = url_length(url)
    url_features.append(i)

    # first directory length
    i = fd_length(url)
    url_features.append(i)

    # count features
    i = get_counts(url)
    url_features.extend(i)

    # digit count
    i = digit_count(url)
    url_features.append(i)

    # letter count
    i = letter_count(url)
    url_features.append(i)

    # number of directories
    i = no_of_dir(url)
    url_features.append(i)

    # presence of IP
    i = having_ip_address(url)
    url_features.append(i)

    # new features
    # subdomain count
    i = subdomain_count(url)
    url_features.append(i)

    # entropy
    i = entropy(url)
    url_features.append(i)

    # digit proportion
    i = digit_proportion(url)
    url_features.append(i)

    # suspicious keywords
    i = suspicious_keyword(url)
    url_features.append(i)

    return url_features
