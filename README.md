# LinkedIn-Data-Extraction

Build Linkedin Dataset Research Proposal
Yin Song
song.yin1@northeastern.edu | 859.583.0161 | Boston, MA | https://www.linkedin.com/in/yin-song/

Summary 
A python script is used to read input CSV, extract LinkedIn information, and write collected data to a new CSV. The implementation and test will take two weeks depends on the requirements of how data is stored, used, and visualized. 

Method
Tools: Python3+
Steps: 
1.	Read the sample CSV data
2.	Conduct data scraping to each LinkedIn page
3.	Extract personal information from each scraped data (name, connections, jobs, etc)
4.	Write extracted information to a new CSV

Code
--I have implemented 40% of a python script to directly extract name, degree, work experience, and connections from a LinkedIn page. Code can be viewed here: https://github.com/songyin79/LinkedIn-Data-Extraction/blob/master/linkedIn_extract.py 

--Sample output of Kevin Boudreau’s LinkedIn:

{'connects': '500+',
 'fname': 'Kevin',
 'grad': 'Master of Arts - MA',
 'lname': 'B.',
 'phd': 'Doctor of Philosophy - PhD',
 'undergrad': 'Bachelor of Applied Science - BASc',
 'works': ['Chief Economist, NASA Tournament Lab',
           'Research Associate: Productivity, Innovation & Entrepreneurship',
           'M&A & Infrastructure Project Program Leader, Latin America',
           'Harvard Business School, Strategy Unit',
           'Professor',
           'Professor, Strategy & Policy',
           'Global Director: Internet, Telecoms & Information Industry '
           'Consulting & Research',
           'Harvard University, Institute of Quantitative Social Science']}


Plan
Time required for implementation: One week
•	Locate tags from scarped data (tags: name, education, etc)
•	Extract data based on tag locations
•	Implement file I/O functions (store data to a database or csv) 
Time required for test and storage: One week
•	Testing
•	Special cases handling such as open folded page section
•	Store/visualize data (depends on requirement) 




