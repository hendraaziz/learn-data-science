class latihan_class():
    #Deklarasi Variabel
    var_nama = ""
    var_alamat = ""
    var_judul = ""
 
    #Membuat Constructor
    def __init__ (self, judul):
        self.var_judul = judul
 
    #fungsi untuk input data variabel
    def get_nama (self, nama):
        self.var_nama = nama
 
    #fungsi untuk input alamat
    def get_alamat(self, alamat):
        self.var_alamat = alamat
 
    #fungsi menampilkan output
    def get_output(self):
        print ("\n\n",self.var_judul)
        print ("Nama : ",self.var_nama)
        print ("Alamat : ", self.var_alamat)
