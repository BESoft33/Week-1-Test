import re
import json

string_sequence = "Get 50% off on every purchase. contact marketing team at market@qq.com. Find all your linkedin " \
                  "contacts for free, jeff.peterson@b2bsearch.com. qq.com partnership program apply at market@qq.com"
sequence = ""
with open('websiteData.txt', 'r', encoding='utf-8') as f:
    sequence = f.read()


def find_all_emails(source: str) -> list:
    all_emails = re.findall(r'[\.a-zA-z0-9]*@[a-zA-z0-9]*\.com', source)
    return all_emails


def filter_emails(emails: list) -> None:
    mails = {}
    for email in emails:
        mails[email] = {
            "Occurrence": 0,
            "EmailType": None
        }

        mails[email]["Occurrence"] = sum([1 for mail in emails if mail == email])

    for em in emails:

        if re.match('[a-zA-z0-9]*\.[a-zA-z0-9]*@[a-zA-z0-9]*\.com', em):
            mails[em]["EmailType"] = "Human"
        else:
            mails[em]["EmailType"] = "Non-Human"

    with open('data.json', 'w') as f:
        json.dump(mails, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    all_mails = find_all_emails(sequence)
    filter_emails(all_mails)

