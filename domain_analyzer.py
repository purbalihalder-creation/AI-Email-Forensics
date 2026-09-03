try:
    import dns.resolver  # type: ignore
except ImportError as e:
    print("Please install dnspython: pip install dnspython")
    raise ImportError("Please install dnspython: pip install dnspython") from e


def get_dns_records(domain):

    result = {
        "A": [],
        "MX": [],
        "NS": []
    }

    for record_type in ["A", "MX", "NS"]:

        try:

            answers = dns.resolver.resolve(
                domain,
                record_type
            )

            for answer in answers:

                result[record_type].append(
                    str(answer)
                )

        except Exception:
            pass

    return result