import vobject
import csv

with open("myContacts.vcf","r",encoding="utf-8") as f:
    vcard_data=f.read()

vcard_list=list(vobject.readComponents(vcard_data))

with open("myContacts.csv","w", newline='',encoding="utf-8") as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(["Full_name","Nickname","Phone"])

    for v in vcard_list:
        full_name=v.fn.value if hasattr(v,'fn') else ''

        nickname=full_name.split()[0] if full_name else ''

        phones = [tel.value for tel in v.contents.get('tel',[])]
        phone_str=', '.join(phones)

        writer.writerow([full_name,nickname,phone_str])
