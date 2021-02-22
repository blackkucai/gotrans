import os
from googletrans import Translator
banner = """\x1b[1;95m
      .-. .-. .-. .-. .-. . . .-. 
      |.. | |  |  |(  |-| |\| `-. 
      `-' `-'  '  ' ' ` ' ' ` `-' 
      Created by blackkucai 2021
\x1b[0m""" 

                                                                     
class transltr:                                                                    
      """ initialize  """     
      def __init__(self):           
          global text
          dict = {
                   'inggris': 'en',
                   'korea': 'ko',
                   'indonesia': 'id',
                   'jepang': 'ja',
                   'perancis': 'fr',
                   'china': 'zh-cn',
                   'rusia': 'ru',
                 }                                              
          os.system('clear')
          translators = Translator()                                                                                               
          print(banner)
          print(' '*10,"Google Translator")
          print()                                    
          text = input('Enter Text to Translate : ')                          
          bahasa = input('Ke bahasa [inggris,korea,indonesia,jepang,perancis]:')               
          try :           
              self.hasil = translators.translate(text, dest=dict[bahasa])
          except Exception as exceptions:
                 print('\x1b[1;91mError:\x1b[0m%s' %(exceptions))                                         
                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
      def run_translt(self):                        
          try:
             print()
             print('dari :', self.hasil.src,":", text)
             print('ke :', self.hasil.dest , ":", self.hasil.text)
             print('pronounce :', self.hasil.pronunciation)     
                                                                                
          except Exception as exceptions:
             print('\x1b[1;91mError:\x1b[0m%s' %(exceptions))
                          
if __name__ == '__main__':                  
   tr = transltr()          
   tr.run_translt()
                       
 

