import csv

csv_columns = ['resume-download', 'name', 'linkedin-title', 'location', 'experience', 'education', 'highlight',
               'fullapplication', '2-year-confirmation', 'exp-years', 'phone', 'resume-filename']

with open("sample.mbox.txt", "r") as f, open("out-v2.csv", 'w', newline='') as c:
    writer = csv.DictWriter(c, fieldnames=csv_columns)
    writer.writeheader()
    
    data = {}
    
    for line in f:
        line = line.strip()
        
        if line == "Download resume:":
            data['resume-download'] = f.readline().strip().replace('amp;', '')
            f.readline()
            data['name'] = f.readline().strip()
            data['linkedin-title'] = f.readline().strip()
            data['location'] = f.readline().strip()
            f.readline()
            f.readline()
            exp = []
            while True:
                l = f.readline().strip()
                if l == "-------------------------------":
                    break
                if l:
                    exp.append(l)
            data['experience'] = exp
            
        elif line == "Education":
            edu = []
            while True:
                l = f.readline().strip()
                if l == "-------------------------------":
                    break
                if l:
                    edu.append(l)
            data['education'] = edu
            
        elif line == "Highlight":
            hig = []
            while True:
                l = f.readline().strip()
                if l == "-------------------------------":
                    break
                if l:
                    hig.append(l)
            data['highlight'] = hig
            
        elif line == "View full application:":
            data['fullapplication'] = f.readline().strip().replace('amp;', '')
            
        elif line == "xyz any content":
            data['2-year-confirmation'] = f.readline().strip()
            
        elif line == "abc any content":
            data['exp-years'] = f.readline().strip()
            
        elif line == "Contact Information":
            f.readline()
            data['phone'] = f.readline().strip().replace('Phone: ', '')
            data['resume-filename'] = f.readline().strip().replace('Resume: ', '')
            
        elif line == "~END~":
            print(data)
            writer.writerow(data)
            data = {}
