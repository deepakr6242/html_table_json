html_data = """

<!DOCTYPE html>
<html>
<body>

<h2>Basic HTML Table</h2>

<table style="width:100%">
  <tr>
    <th>Firstname</th>
    <th>Lastname</th> 
    <th>Age</th>
  </tr>
  <tr>
    <td>Jill</td>
    <td>Smith</td>
    <td>50</td>
  </tr>
  <tr>
    <td>Eve</td>
    <td>Jackson</td>
    <td>94</td>
  </tr>
  <tr>
    <td>John</td>
    <td>Doe</td>
    <td>80</td>
  </tr>
</table>


<table style="width:100%">
  <tr>
    <th>language</th>
    <th>version</th> 
    <th>os</th>
  </tr>
  <tr>
    <td>python</td>
    <td>2.7</td>
    <td>windows</td>
  </tr>
  <tr>
    <td>Java</td>
    <td>8</td>
    <td>linux</td>
  </tr>
  <tr>
    <td>php</td>
    <td>2.5</td>
    <td>ubuntu</td>

  </tr>
</table>

</body>
</html>

 """

from bs4 import BeautifulSoup
import json
#table_data = [[cell.text for cell in row("td")]
                         #for row in BeautifulSoup(html_data,'html.parser')("tr")]

#print table_data

#import json
#print json.dumps(dict(table_data))

soup = BeautifulSoup(html_data,'html.parser')

headers = [] 
for table in soup.find_all('table'):
  
  for row in table.find_all('tr'):
          if  row.find('th'):
            #print  row.text.strip().split('\n')
            headers.append(row.text.strip().split('\n'))
            #print "--------"
             
#print headers
with open('demo.json','w') as f:    
    count = 0 
    for table in soup.find_all('table'):
      keys = [th.get_text(strip=True)for th in table.find_all('th')
             
      values = [td.get_text() for td in table.find_all('tr')] 
      f.write('table'+str(count)+'\n')
      for i in values[1:]:
        print dict(zip(keys,i.split()))
        print '--------'
        json.dump(dict(zip(keys,i.split())),f)
        f.write('\n')
      count+=1


    
   






