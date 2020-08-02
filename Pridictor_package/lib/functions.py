from urllib import parse
from socket import gethostbyname
from re import compile, findall
import ipaddress
from sklearn.preprocessing import StandardScaler


def start_url(url):
    # decode url
    url = parse.unquote_plus(url.strip())
    """Split URL into: protocol, host, path, params, query and fragment."""
    if not parse.urlparse(url.strip()).scheme:
        url = "http://" + url
    protocol, host, path, params, query, fragment = parse.urlparse(url.strip())

    result = {
        "url": host + path + params + query + fragment,
        "protocol": protocol,
        "host": host,
        "path": path,
        "params": params,
        "query": query,
        "fragment": fragment,
    }
    return result


def count(text, character):
    """Return the amount of certain character in the text."""
    return text.count(character)


def count_charater(text):
    """ Return Characte count in text"""
    pattern = "[a-zA-z]"
    return len(findall(pattern, text))


def count_digit(text):
    """ Return digit count in text"""
    pattern = "[0-9]"
    digt_count = len(findall(pattern, text))
    if digt_count != 0:
        return digt_count
    else:
        return 1


def count_non_alphanumerical(text):
    """ Return digit count in text"""
    pattern = "[^0-9a-zA-Z_]"
    return len(findall(pattern, text))


def count_vowels(text):
    """Return the number of vowels."""
    pattern = "[aeiouAEIOU]"
    return len(findall(pattern, text))


def count_consonant(text):
    """Return the number of consonant."""
    pattern = "[^aeiouAEIOU]"
    con_len = len(findall(pattern, text))
    if con_len != 0:
        return con_len
    else:
        return 1


def count_params(text):
    """Return number of parameters."""
    return len(parse.parse_qs(text))


def valid_ip(text):
    """Return if the domain has a valid IP format (IPv4 or IPv6)."""
    try:
        ipaddress.ip_address(text)
        return 1
    except Exception:
        return 0


def host_has_ip(text):
    """Return if host have a ip address"""
    try:
        if gethostbyname(text):
            return 1
        else:
            return 0
    except:
        return 0


def find_http(text):
    """Return if http or htpps present in  text"""
    if "http" in text.lower() or "https" in text.lower():
        return 1
    else:
        return 0


def count_tld_url(text):
    """Return amount of Top-Level Domains (TLD) present in the URL."""
    path = r"lib\files"
    file = open(path + r"\tlds.txt", "r")
    count = 0
    pattern = compile("[a-zA-Z0-9.]")
    for line in file:
        i = (text.lower().strip()).find(line.strip())
        while i > -1:
            if ((i + len(line) - 1) >= len(text)) or not pattern.match(
                text[i + len(line) - 1]
            ):
                count += 1
            i = text.find(line.strip(), i + 1)
    file.close()
    return count


def avg_len_tokens(url):
    """return Average length tokens in of url"""
    url = parse.unquote_plus(url.strip())
    if not parse.urlparse(url.strip()).scheme:
        url = "http://" + url
    o = parse.urlparse(url)
    if o.scheme:
        len_scheme = len(str(o.scheme))
    else:
        len_scheme = 0
    if o.netloc:
        len_netloc = len(str(o.netloc))
    else:
        len_netloc = 0
    if o.path:
        len_path = len(str(o.path))
    else:
        len_path = 0
    if o.params:
        len_params = len(str(o.params))
    else:
        len_params = 0
    if o.query:
        len_query = len(str(o.query))
    else:
        len_query = 0
    if o.fragment:
        len_fragment = len(str(o.fragment))
    else:
        len_fragment = 0
    if o.username:
        len_username = len(str(o.username))
    else:
        len_username = 0
    if o.password:
        len_password = len(str(o.password))
    else:
        len_password = 0
    if o.hostname:
        len_hostname = len(str(o.hostname))
    else:
        len_hostname = 0

    avg = (
        len_scheme
        + len_path
        + len_fragment
        + len_hostname
        + len_netloc
        + len_params
        + len_password
        + len_username
        + len_query
    ) / 9

    return avg


def Feature(url):
    feature_dict_url = {}
    lable = [
        "url",
        "url_len",
        "count_comma",
        "count_semicolon",
        "count_quotes",
        "count_braces",
        "count_redirects",
        "count_pipes",
        "count_dots",
        "count_dash",
        "count_underline",
        "count_question",
        "count_equal",
        "count_attherate",
        "count_char",
        "count_digit",
        "count_alphanumeric",
        "count_non_alphanumeric",
        "count_tlds",
        "host_has_ip",
        "present_ip",
        "present_http",
        "count_dots_host",
        "count_digit_host",
        "count_non_alphanumeric_host",
        "parameter_count",
        "parameter_length",
        "directory_len",
        "digit_char_ratio",
        "vowel_consonant_ratio",
        "avg_len_token",
    ]
    dict_url = start_url(url)
    url_length = len(dict_url["url"])
    commas_count = count(dict_url["url"], ",")
    semicolon_count = count(dict_url["url"], ";")
    quotes_count = count(dict_url["url"], '"') + count(dict_url["url"], "'")
    braces_count = (
        count(dict_url["url"], "{")
        + count(dict_url["url"], "}")
        + count(dict_url["url"], "(")
        + count(dict_url["url"], ")")
        + count(dict_url["url"], "[")
        + count(dict_url["url"], "]")
    )
    redirect_count = count(dict_url["url"], "//")
    pipes_count = count(dict_url["url"], "|")
    dot_count = count(dict_url["url"], ".")
    dash_count = count(dict_url["url"], "-")
    underline_count = count(dict_url["url"], "_")
    question_count = count(dict_url["url"], "?")
    equal_count = count(dict_url["url"], "=")
    attherate_count = count(dict_url["url"], "@")
    char_count = count_charater(dict_url["url"])
    digit_count = count_digit(dict_url["url"])
    alphanumerical_count = char_count + digit_count
    non_alphanumerical_count = count_non_alphanumerical(dict_url["url"])
    count_tld = count_tld_url(dict_url["url"])
    # Host based
    host_ip = host_has_ip(dict_url["host"])
    having_ip = valid_ip(dict_url["host"])
    having_http = find_http(dict_url["host"])
    dot_count_host = count(dict_url["host"], ".")
    digit_count_host = count_digit(dict_url["host"])
    non_alphanumerical_count_host = count_non_alphanumerical(dict_url["host"])
    # parameter based
    if dict_url["query"]:
        parameter_count = count_params(dict_url["url"])
        parameter_length = len(dict_url["query"])
    else:
        parameter_count = 0
        parameter_length = 0
    # directory based
    if dict_url["path"]:
        path_length = len(dict_url["path"])
    else:
        path_length = 0
    # ratio base feature
    digit_char_ratio = char_count / digit_count
    vowel_consonant_ratio = count_vowels(dict_url["url"]) / count_consonant(
        dict_url["url"]
    )
    avglen_tokens = avg_len_tokens(url)
    url = parse.unquote_plus(url.strip())
    var_ls = [
        r"{}".format(url),
        url_length,
        commas_count,
        semicolon_count,
        quotes_count,
        braces_count,
        redirect_count,
        pipes_count,
        dot_count,
        dash_count,
        underline_count,
        question_count,
        equal_count,
        attherate_count,
        char_count,
        digit_count,
        alphanumerical_count,
        non_alphanumerical_count,
        count_tld,
        host_ip,
        having_ip,
        having_http,
        dot_count_host,
        digit_count_host,
        non_alphanumerical_count_host,
        parameter_count,
        parameter_length,
        path_length,
        digit_char_ratio,
        vowel_consonant_ratio,
        avglen_tokens,
    ]
    # for i in range(len(lable)):
    #     feature_dict_url[lable[i]] = var_ls[i]
    # return feature_dict_url
    sc_x = StandardScaler()
    X_scaled = sc_x.fit_transform([var_ls[1:]])
    return X_scaled
