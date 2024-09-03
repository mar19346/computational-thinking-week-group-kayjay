import pandas as pd
from io import StringIO

data = """
Name,Role,Learning Team
Aya Abdelrahman,Student,Learning Team 5
Wahideh Achbari,Teacher,Staff
Bissola Adenekan,Student,Learning Team 1
Roland Adorjani,Teacher,Staff
Shriya Agrawal,Student,Learning Team 5
Gizem Aktas,Teacher,Learning Team 5
Ava Ali,Student,Learning Team 1
Sean Almeida,Student,Learning Team 2
Lukas Ansteeg,Teacher,Staff
Maja Arament,Student,Learning Team 2
Theo Araujo,Teacher,Staff
Gadis Arumcitta Gadis Masita,Student,Learning Team 3
Dorottya Báldy,Student,Learning Team 4
Lotte Becking,Student,Learning Team 4
Gabriella Beckley,Student,Learning Team 3
Alejandro Berges Coronel,Student,Learning Team 3
Julius Bijkerk,Teacher,Learning Team 2
Emma-Rose Blacher,Student,Learning Team 2
Rasmus Blichfeldt,Student,Learning Team 1
Tommy Blomvliet,Teacher,Staff
Penelope Bollini,TA,Learning Team 3
Lumi Borgers,Student,Learning Team 5
Christal Breinburg,Student,Learning Team 1
Irene Bressanello,Student,Learning Team 2
Anouk Buijs,Student,Learning Team 5
Volodymyr Butko,Student,Learning Team 4
Catherin Catherin Andiani,Student,Learning Team 1
Alva Chen,Student,Learning Team 4
Roy Chen,Student,Learning Team 3
Nikko Chy,Student,Learning Team 3
Ana Contreras Estrada,Student,Learning Team 2
Walter Contreras Estrada,Student,Learning Team 5
Brendan Corcoran,Student,Learning Team 4
Joeben Davis,Student,Learning Team 5
Philine Dekker,Student,Learning Team 1
Maria Dumitru,Student,Learning Team 5
Farah Elhusseini,Student,Learning Team 1
Alexandru Enache,Student,Learning Team 2
Wentao Fan,Student,Learning Team 3
Felicia Felicia Christy Leo,Student,Learning Team 3
Jacco Friedeberg,Student,Learning Team 2
Márton Gera,TA,Learning Team 1
Callum Ginsburg,Student,Learning Team 4
Angelica Goetzen,Teacher,Staff
Ömer Gökçe,Student,Learning Team 2
Alon Goodall,Teacher,Learning Team 5
Kimiya Gräfin Zu Eltz,Student,Learning Team 2
mirre Grouls,Student,Learning Team 1
Davide Hanna,Student,Learning Team 5
Leon Heemskerk,Student,Learning Team 5
Barbara ten Hoedt,Teacher,Staff
Micay van Hoogdalem,Student,Learning Team 3
Andre Hua,Student,Learning Team 2
Calson Huang,Student,Learning Team 5
Adam Humphreys,Student,Learning Team 1
Elnara Ibrahimli,Student,Learning Team 3
Angela Iversen,Student,Learning Team 4
Mana Iwasaki,Student,Learning Team 3
Khushi Jain,Student,Learning Team 4
Regina Jarillo Romo,Student,Learning Team 4
Ilias Jelasity,Student,Learning Team 5
Danielius Jonaitis,Student,Learning Team 4
Sophia Khinchikashvili,Student,Learning Team 5
Scarlett Kim,Student,Learning Team 1
Sina Kitapci,Student,Learning Team 3
Anna Klinker,Student,Learning Team 5
Markus Knell,Student,Learning Team 5
Maximilian Koch,Student,Learning Team 1
Tadas Kraujalis,Student,Learning Team 3
Akira Kuno,Student,Learning Team 4
Jamie Lee,Student,Learning Team 2
Daniel Lefenda,Student,Learning Team 3
David Liebmann,Student,Learning Team 4
Noel Lilliestielke,Student,Learning Team 4
Yujia Liu,Student,Learning Team 2
Gabriela Mahecha Califa,Student,Learning Team 4
Rafael Mantoani,Student,Learning Team 1
Daniel Mayerhoffer,Teacher,Learning Team 1
Maartje Meijers,Teacher,Staff
Josy Mertens,Student,Learning Team 1
Kazuya Nagai,Student,Learning Team 4
Lucas Nagtegaal,Student,Learning Team 5
Eugenia Natasha,TA,Learning Team 5
Koyo Natsume,Student,Learning Team 2
Alexia Nichifor,Student,Learning Team 3
Viktor Nobel,Student,Learning Team 3
Dasha Opoku-Gyamfi,Student,Learning Team 5
Clement Paitrault,Student,Learning Team 3
Lisa van Pappelendam,Teacher,Staff
Viggo Pauw,Student,Learning Team 2
Laura Peirs,TA,Staff
Thaïss Petit,Student,Learning Team 5
Steven Pickering,Teacher,Learning Team 3
Diogo da Piedade Baptista,Student,Learning Team 3
Thomas Poell,Teacher,Staff
Gaspar Prieto Pote Monteiro Nogueira,Student,Learning Team 3
Abhijit Raghu,Student,Learning Team 1
Asjfaaq Razab-Sekh,Student,Learning Team 4
Leon van Rooijen,Teacher,Staff
Alexandra Roskam,Student,Learning Team 3
Cem Şahingiray,Student,Learning Team 4
Maria Sałasińska,Student,Learning Team 1
Federico Santi,Student,Learning Team 2
Nia Sas,Student,Learning Team 1
Melody Scales,Student,Learning Team 2
Michelle Schimmel,TA,Learning Team 4
Bianka Śledzińska,Student,Learning Team 5
Porter Stacy,Student,Learning Team 1
Nojus Stankevičius,Student,Learning Team 1
Anna Szwedowska,Student,Learning Team 1
Emilie Taffouraud,Student,Learning Team 5
Lucia Tanco Alonso,Student,Learning Team 2
Mark Temchenko,Student,Learning Team 3
Antonín Tesař,Student,Learning Team 4
Niki Thrasyvoulou,Student,Learning Team 4
Kaleem Ullah,Teacher,Learning Team 3
Diliara Valeeva,Teacher,Staff
Antonio Vasto,Student,Learning Team 4
Rick Verplanke,Teacher,Staff
Merijn Vervoorn,Student,Learning Team 3
Emma Verweij,Teacher,Staff
Juliette Visser,Student,Learning Team 2
Bey Vongpatanasin,Student,Learning Team 5
Weizhao Wang,Student,Learning Team 2
David Wild,Student,Learning Team 1
Rens Wilderom,Teacher,Staff
Kim van Winsen,Teacher,Staff
Collins Woodbleach,Student,Learning Team 1
Wu Ke Wu,Student,Learning Team 5
Derrick Wyckelsma,Student,Learning Team 2
Sihun You,Student,Learning Team 3
In Hyeok Youn,Student,Learning Team 2
Shuting Yu,Student,Learning Team 4
Marwan Zeinalabidin,Student,Learning Team 4
Meng Zhao,Student,Learning Team 1
Fleming Ziehm,Student,Learning Team 5
"""

df = pd.read_csv(StringIO(data))
df = df[~df['Role'].isin(['Teacher', 'TA'])]
df = df.drop(columns=['Role'])
df = df.drop_duplicates(subset=['Name'])
df['Name'] = df['Name'].str.split(' ').str[0]
df['Learning Team'] = df['Learning Team'].str.split(' ').str[-1]

def solution_station_5(name):
    if name in df['Name'].values:
        return df[df['Name'] == name]['Learning Team'].values[0]
    else:
        return False