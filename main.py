import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QFileDialog
from ui.Ui_octopus_editor import Ui_MainWindow
from readfile import Readfile
from llm import LLM_using
import os
 
class MyMainWindow(QMainWindow,Ui_MainWindow):
    sequence_now=""
    sequence_id_now=""
    sequence_path_now=""
    completed_sequence=""

    def __init__(self,parent=None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)

    def trigger_actHelp(self):
        QMessageBox.about(self,"about","""Octopus_Editor v0.0.1\nCopyright 2025 Dr0ctopus1145\nAll rights reserved\nContact me with email 3230100794@zju.edu.cn""")

    def trigger_actOpen(self):
        file_path, _ = QFileDialog.getOpenFileName(self,"choose a file","./data/","Fasta Files (*.fasta)")
        info=Readfile.read_fasta_file(file_path)
        self.sequence_path_now=file_path
        self.sequence_now=" ".join(list(info[1]))
        self.sequence_id_now=info[0]
        self.textEdit.setText(self.sequence_now)
        #print(info[0])
        self.textBrowser_2.setText(info[0])
        return
    
    def trigger_actClose(self):
        self.textEdit.setText("")
        self.textBrowser_2.setText("")
        self.sequence_now=""
        self.completed_sequence=""
        self.sequence_path_now=""
        self.sequence_id_now=""
        return

    def send_sequence_to_LLM(self):
        input=self.textEdit.toPlainText()
        completed_sequence=LLM_using.LLM_using(input)
        self.textBrowser.setText("the completed sequence with highest score:"+completed_sequence)
        self.completed_sequence="".join(completed_sequence.split())
        return
    
    def save(self):
        content=">"+self.sequence_id_now+"\n"+"".join(self.textEdit.toPlainText().split())
        with open(self.sequence_path_now, 'w', encoding='utf-8') as f:
            f.writelines(content)
        return
    
    def save_as(self):
        content=">"+self.sequence_id_now+"\n"+"".join(self.textEdit.toPlainText().split())
        file_path, _ = QFileDialog.getSaveFileName(self,"save as",os.path.expanduser("./data/"+self.sequence_id_now+".fasta"),"fasta file(*.fasta)")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return

    def save_the_completed(self):
        content=">completed_"+self.sequence_id_now+"\n"+self.completed_sequence
        file_path, _ = QFileDialog.getSaveFileName(self,"save as",os.path.expanduser("./data/completed_"+self.sequence_id_now+".fasta"),"fasta file(*.fasta)")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return
    
if __name__=='__main__':
    app=QApplication(sys.argv)
    myWin=MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
    