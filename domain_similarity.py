from difflib import SequenceMatcher
def domain_similarity(domain, legitimate_domain):

    return SequenceMatcher(None, domain.lower(), legitimate_domain.lower()).ratio()