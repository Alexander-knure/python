
#21. Создать иерархию классов Электронная вычислительная
#машина, Персональный компьютер, Ноутбук. Класс Электронная
#вычислительная машина должен содержать атрибуты и методы, общие для
#производных классов. Основная программа должна создавать массивы
#объектов производных классов и выводить их на экран.
from abc import ABC, abstractmethod
import colorama
from colorama import Fore, Back, Style
colorama.init()

class EVM(ABC):
    __Name = None 
    __Producer = None 
    __OS = None 

    __CPU_Name = None 
    __CPU_Type = None 
    __CPU_Clock = 0.0
    __CPU_Cores = 0
    __CPU_Threads = 0

    __Motherboard = None 
    __Socket = None 
    __SoundCard = None 
    __VideoOutput = None 
    __USBs = 0
    __isBluetooth = False
    __isWiFi = False

    __GPU_Name = None 
    __GPU_Clock = 0.0
    __VRAM = 0
    __isIntegratedGPU = False

    __RAM = 0
    __RAM_Type = None 
    __RAM_Slots = 0
    __ROM = 0
    __isSSD = False
    __isDVD = False

    __Height = 0.0
    __Length = 0.0
    __Width = 0.0
    
    def __init__(self, Name, Produce, OS):
         self. __Name = Name
         self.__Producer = Produce
         self.__OS = OS

    @abstractmethod
    def setCPU(self, CPU_Name, CPU_Type, CPU_Clock, CPU_Cores, isSMT):
        self.__CPU_Name = CPU_Name
        self.__CPU_Type = CPU_Type
        try:
            if float(CPU_Clock) > 0:
                self.__CPU_Clock = float(CPU_Clock)
            elif float(CPU_Clock) < 0:
                print("Error: CPU clock < 0")
            else:
                print("Error: CPU clock = 0")
        except ValueError:
               print("Error: CPU clock is not a number")

        try:
            if int(CPU_Cores) > 0:
                self.__CPU_Cores = int(CPU_Cores)
                if isSMT == True:
                    self.__CPU_Threads = CPU_Cores * 2
                else:
                     self.__CPU_Threads = CPU_Cores
            elif int(CPU_Cores) < 0:
                print("Error: CPU cores < 0")
            else:
                print("Error: CPU cores = 0")
        except ValueError:
               print("Error: CPU cores is not a number")

    @abstractmethod
    def setMotherboard(self, Motherboard, Socket, SoundCard, VideoOutput, USBs, isBluetooth, isWiFi):
         self.__Motherboard = Motherboard
         self.__Socket = Socket
         self.__SoundCard = SoundCard
         self.__VideoOutput = VideoOutput

         try:
            if int(USBs) > 0:
                self.__USBs = int(USBs)
            elif int(USBs) < 0:
                print("Error: USB count < 0")
         except ValueError:
               print("Error: USB count is not a number")

         self.__isBluetooth = isBluetooth
         self.__isWiFi = isWiFi
   
    @abstractmethod
    def setGPU(self, GPU_Name, GPU_Clock, VRAM, isIntegratedGPU):
          self.__GPU_Name = GPU_Name

          try:
            if float(GPU_Clock) > 0:
                self.__GPU_Clock = float(GPU_Clock)
            elif float(GPU_Clock) < 0:
                print("Error: GPU clock < 0")
            else:
                print("Error: GPU clock = 0")
          except ValueError:
               print("Error: GPU clock is not a number")
          self.__GPU_Clock = GPU_Clock
         
          if(isIntegratedGPU == True):
             self.__isIntegratedGPU = isIntegratedGPU
             if VRAM == 0:    
                print("GPU is intergated! VRAM works by a different formula")
                self.__VRAM = self.__RAM * 0.1
             else:
                self.__VRAM = VRAM
          else:
             try:
                if int(VRAM) > 0:
                    self.__VRAM = int(VRAM)
                elif int(VRAM) < 0:
                    print("Error: VRAM < 0")
                else:
                    print("Error: VRAM = 0 and GPU isn`t integrated")
             except ValueError:
                    print("Error: VRAM is not a number")

    @abstractmethod
    def setMemory(self, RAM, RAM_Type, RAM_Slots, ROM, isSSD, isDVD):
            try:
                if int(RAM) > 0:
                    self.__RAM = int(RAM)
                elif int(RAM) < 0:
                    print("Error: RAM < 0")
                else:
                    print("Error: RAM = 0")
            except ValueError:
                    print("Error: RAM is not a number")
            self.__RAM_Type = RAM_Type
            try:
                if int(RAM_Slots) > 0:
                    self.__RAM_Slots = int(RAM_Slots)
                elif int(RAM) < 0:
                    print("Error: RAM slots < 0")
                else:
                    print("Error: RAM slots = 0")
            except ValueError:
                    print("Error: RAM slots is not a number")
            try:
                if int(ROM) > 0:
                    self.__ROM = int(ROM)
                elif int(RAM) < 0:
                    print("Error: ROM < 0")
                else:
                    print("Error: ROM = 0")
            except ValueError:
                    print("Error: ROM is not a number")

            self.__isSSD = isSSD
            self.__isDVD = isDVD

    @abstractmethod
    def setCase(self, Height, Length, Width):
            try:
                if float(Height) > 0:
                    self.__Height = float(Height)
                elif float(Height) < 0:
                    print("Error: Height < 0")
                else:
                    print("Error: Height = 0")
            except ValueError:
                   print("Error: Height is not a number")
            try:
                if float(Length) > 0:
                    self.__Length = float(Length)
                elif float(Length) < 0:
                    print("Error: Length < 0")
                else:
                    print("Error: Length = 0")
            except ValueError:
                   print("Error: Length is not a number")
            try:
                if float(Width) > 0:
                    self.__Width = float(Width)
                elif float(Width) < 0:
                    print("Error: Width < 0")
                else:
                    print("Error: Width = 0")
            except ValueError:
                   print("Error: Width is not a number")

    def printShortInformaton(self):
         print("Information about: " + Fore.BLUE + self.__Name + Style.RESET_ALL)
         print("Producer:", self.__Producer)
         print("OS:", self.__OS)
        
    @abstractmethod
    def printFullInformaton(self):
         self.printShortInformaton()

         if(self.__CPU_Name != None):
            print(Fore.YELLOW + "Information about CPU:" + Style.RESET_ALL)
            print("Name:", self.__CPU_Name)
            print("Type:", self.__CPU_Type)
            print("Clock:", self.__CPU_Clock, "GHz")
            print("Cores:", self.__CPU_Cores) 
            if self.__CPU_Cores * 2 == self.__CPU_Threads and self.__CPU_Cores != 0:
               print("SMT/HT:",  True)
            else:
               print("SMT/HT:",  False)
            print("Threads:", self.__CPU_Threads)
         else:
            print(Fore.RED +"Information about CPU: not installed :(" + Style.RESET_ALL)

         if(self.__Motherboard != None):
            print(Fore.YELLOW +"Information about motherboard:" + Style.RESET_ALL)
            print("Name:", self.__Motherboard)
            print("Socket:", self.__Socket)
            print("Sound card:", self.__SoundCard)
            print("Video output:", self.__VideoOutput)
            print("Number of USB:", self.__USBs)
            print("Bluetooth:", self.__isBluetooth)
            print("Wi-Fi:", self.__isWiFi)
         else:
            print(Fore.RED +"Information about motherboard: not installed :(" + Style.RESET_ALL)

         if(self.__GPU_Name != None):
            print(Fore.YELLOW +"Information about GPU:" + Style.RESET_ALL)
            print("Name:", self.__GPU_Name)
            print("Clock:", self.__GPU_Clock, "MHz")
            print("VRAM:", self.__VRAM, "GB")
            print("Integrated GPU:", self.__isIntegratedGPU)
         else:
            print(Fore.RED +"Information about GPU: not installed :(" + Style.RESET_ALL)

         if(self.__RAM != 0):
            print(Fore.YELLOW +"Information about memory:" + Style.RESET_ALL)
            print("RAM:", self.__RAM, "GB")
            print("Number of slots:", self.__RAM_Slots)
            print("ROM:", self.__ROM, "GB")
            if self.__isSSD == True:
               print("ROM is SSD")
            else:
               print("ROM is HDD")
            if self.__isDVD == True:
               print("Device has a DVD drive")
            else:
                print("Device hasn`t a DVD drive")
         else:
            print(Fore.RED +"Information about memory: not installed :(" + Style.RESET_ALL)
     
class PC(EVM):
    __CaseForm = None 

    __Fans = 0
    __CoolingSystem = None

    __PSU_Name = None
    __PSU_Sertification = None
    __PSU_Energy = 0
   
    __MotherboardForm = None

    def setCPU(self, CPU_Name, CPU_Type, CPU_Clock, CPU_Cores, isSMT):
        return super().setCPU(CPU_Name, CPU_Type, CPU_Clock, CPU_Cores, isSMT)

    def setGPU(self, GPU_Name, GPU_Clock, VRAM, isIntegratedGPU):
        return super().setGPU(GPU_Name, GPU_Clock, VRAM, isIntegratedGPU)

    def setMemory(self, RAM, RAM_Type, RAM_Slots, ROM, isSSD, isDVD):
        return super().setMemory(RAM, RAM_Type, RAM_Slots, ROM, isSSD, isDVD)

    def setCase(self, Height, Length, Width, CaseForm):
        self.__CaseForm = CaseForm
        return super().setCase(Height, Length, Width)

    def setMotherboard(self, Motherboard, Socket, SoundCard, VideoOutput, USBs, isBluetooth, isWiFi, MotherboardForm):
        self.__MotherboardForm = MotherboardForm
        return super().setMotherboard(Motherboard, Socket, SoundCard, VideoOutput, USBs, isBluetooth, isWiFi)

    def setCooling(self,Fans,CoolingSystem):
         try:
                if int(Fans) > 0:
                    self.__Fans = int(Fans)
                elif int(Fans) < 0:
                    print("Error: Number of fans < 0")
                else:
                    print("Warning: PC hasn`t fans")
                    self.__Fans = int(Fans)
         except ValueError:
                    print("Error: Number of fans is invalid data")
         self.__CoolingSystem = CoolingSystem

    def setPSU(self, PSU_Name, PSU_Sertification, PSU_Energy):
            self.__PSU_Name = PSU_Name
            self.__PSU_Sertification = PSU_Sertification
            try:
                if int(PSU_Energy) > 0:
                    self.__PSU_Energy = int(PSU_Energy)
                elif int(PSU_Energy) < 0:
                    print("Error: PSU energy < 0")
                else:
                    print("Error: PSU energy = 0")
            except ValueError:
                    print("Error: PSU energy is not a number")

    def printFullInformaton(self):
        super().printFullInformaton()
        if(self._EVM__Height != 0):
            print(Fore.YELLOW +"Information about case:" + Style.RESET_ALL)
            print("Height:", self._EVM__Height)
            print("Width:", self._EVM__Width)
            print("Length:", self._EVM__Length)
            print("Form:", self.__CaseForm)
            print("Motherboard size:", self.__MotherboardForm)
        else:
            print(Fore.RED +"Information about case: not installed :(" + Style.RESET_ALL)

        if(self.__CoolingSystem != None):
            print(Fore.YELLOW +"Information about cooling system:" + Style.RESET_ALL)
            print("Name CS on CPU:", self.__CoolingSystem)
            print("Number of fans:", self.__Fans)
        else:
            print(Fore.RED +"Information about cooling system: not installed :(" + Style.RESET_ALL)

        if(self.__PSU_Name != None):
            print(Fore.YELLOW +"Information about power supply unit:" + Style.RESET_ALL)
            print("Name:", self.__PSU_Name)
            print("Power:", self.__PSU_Energy," W")
            print("Sertification:", self.__PSU_Sertification)
        else:
            print(Fore.RED +"Information about PSU: not installed :(" + Style.RESET_ALL)
            
        print()

class Laptop(EVM):
    __Type = None
    __Material = None 
    __Weight = 0.0

    __Accumulator = 0.0
    
    __DisplaySize = 0.0
    __DisplayResolution = None
    __DisplayType = None
    __isDisplaySensory =False

    __isFrontCam = False
    __isKeyboardBacklight = False
    __isNumPad = False

    def setCPU(self, CPU_Name, CPU_Clock, CPU_Cores, isSMT):
        return super().setCPU(CPU_Name, "BGA", CPU_Clock, CPU_Cores, isSMT)

    def setGPU(self, GPU_Name, GPU_Clock, VRAM, isIntegratedGPU):
        return super().setGPU(GPU_Name, GPU_Clock, VRAM, isIntegratedGPU)

    def setMemory(self, RAM, RAM_Slots, ROM, isSSD, isDVD):
        return super().setMemory(RAM, "SODIMM", RAM_Slots, ROM, isSSD, isDVD)

    def setCase(self, Height, Length, Width, Type, Material, Weight):
        self.__Type = Type
        self.__Material = Material
        try:
                if float(Weight) > 0:
                    self.__Weight = float(Weight)
                elif float(Weight) < 0:
                    print("Error: Weight < 0")
                else:
                    print("Error: Weight = 0")
        except ValueError:
                   print("Error: Weight is not a number")
        return super().setCase(Height, Length, Width)

    def setMotherboard(self, Motherboard, Socket, SoundCard, VideoOutput, USBs, isBluetooth, isWiFi):
        return super().setMotherboard(Motherboard, Socket, SoundCard, VideoOutput, USBs, isBluetooth, isWiFi) 
 
    def setAccumulator(self, Accumulator):
        try:
                if float(Accumulator) > 0:
                    self.__Accumulator = float(Accumulator)
                elif float(Accumulator) < 0:
                    print("Error: Accumulator < 0")
                else:
                    print("Error: Accumulator = 0")
        except ValueError:
                   print("Error: Accumulator is not a number")

    def setDisplay(self,DisplaySize,DisplayResolution,DisplayType,isDisplaySensory):
            try:
                if float(DisplaySize) >= 10 and float(DisplaySize) < 20:
                    self.__DisplaySize = float(DisplaySize)
                elif float(DisplaySize) > 20:
                    print("Error: Display size >= 20")
                else:
                    print("Error: Display size < 10")
            except ValueError:
                   print("Error: Display size is not a number")

            s = DisplayResolution.split('x')
            isCorrectRes = False
            try:
                for res in s:
                        if int(res) < 100 and int(res) > 10000:
                            isCorrectRes = False
                            print("Error: Display resolution should be in the range of 100 to 10,000")
                        else:
                            isCorrectRes = True
            except ValueError:
                    isCorrectRes = False
                    print("Error: Number of fans is invalid data")

            if isCorrectRes:
                self.__DisplayResolution = DisplayResolution
            else:
                self.__DisplayResolution = None 

            self.__DisplayType = DisplayType
            self.__isDisplaySensory =isDisplaySensory


    def setExtra(self,isFrontCam,isKeyboardBacklight, isNumPad):
        self.__isFrontCam = isFrontCam 
        self.__isKeyboardBacklight = isKeyboardBacklight 
        self.__isNumPad = isNumPad 

    def printFullInformaton(self):
        super().printFullInformaton()

        if(self.__Type != None):
            print(Fore.YELLOW +"Information about case:" + Style.RESET_ALL)
            print("Type:", self.__Type)
            print("Material:", self.__Material)
            print("Weight:", self.__Weight,"kg")
        else:
            print(Fore.RED +"Information about case: not installed :(" + Style.RESET_ALL)

        if(self.__DisplayType != None):
            print(Fore.YELLOW +"Information about display:" + Style.RESET_ALL)
            print("Size:", self.__DisplaySize, "inch")
            print("Resolution:", self.__DisplayResolution)
            print("Type:", self.__DisplayType)
            print("Sensory:", self.__isDisplaySensory)
        else:
            print(Fore.RED +"Information about display: not installed :(" + Style.RESET_ALL)

        if(self.__Accumulator != 0):
            print(Fore.YELLOW +"Information about accumulator:" + Style.RESET_ALL)
            print("Capacty:", self.__Accumulator,"kWh")
        else:
            print(Fore.RED +"Information about accumulator: not installed :(" + Style.RESET_ALL)

        print(Fore.YELLOW +"Information about other functions:" + Style.RESET_ALL)
        print("Front camera: ",self.__isFrontCam)
        print("Backlight of keyboard: ",self.__isKeyboardBacklight)
        print("Numeric keypad: ",self.__isNumPad)

        print()
       
def Main():
    EVMs =[]
    print(Fore.GREEN + "Laptop test:" + Style.RESET_ALL)
    EVMs.append(Laptop("ASUS ZENBOOK PRO UX501JW", "ASUS", "Windows 10 Home x64"))
    EVMs.append(Laptop("ASUS ZENBOOK PRO UX501YJ", "ASUS", "Ubuntu 19.10 LTS"))
    EVMs.append(Laptop("ASUS ZENBOOK PRO UX501VW", "ASUS", "Windows 10 Pro x64"))
    
    for l in EVMs:
        l.setCase(2,30,50,"professional","aluminium",2.01)
        l.setCPU("Intel Core i7-6700HQ", 3.5, 4, True)
        l.setMemory(16, 1, 512, True, False)
        l.setGPU("NVIDIA GeForce GTX 960M", 1127, 4, True)
        l.setMotherboard("Intel HM170", "Intel Skylake PCH-H High DAC","FCBGA1440","HDMI, DisplayPort",4,True,True)
        l.setDisplay(15.6, "3840x2160", "IPS", True)
        l.setAccumulator(96)
        l.setExtra(True, True, True)

    EVMs[0].printShortInformaton()
    EVMs[1].printShortInformaton()
    print()
    EVMs[2].printFullInformaton()

    print(Fore.GREEN + "PC test:" + Style.RESET_ALL)
    EVMs.append(PC("NUC BOXNUC7I", "Intel", "DOS"))
    EVMs.append(PC("OptiPlex 7070 UFF Ultra mini-PC", "Dell", "Windows 10 Pro x64"))
    EVMs.append(PC("ThinkCentre M72e", "Lenovo", "Endless"))
    EVMs.append(PC("Mac Pro A1991 (Z0W3001FW)", "Apple", "macOS Catalina"))
    for p in EVMs:
        p.printShortInformaton()
    print()
    EVMs.append(PC("D340MC", "ASUS", "No"))
    EVMs[4].setCase(160, 378, 355, "Miditower")
    EVMs[4].setCooling(1, "No")
    EVMs[4].setPSU("FrimeCom SM350BL", "80 PLUS", 350)
    EVMs[4].printFullInformaton()
    EVMs.append(PC("Matrexx 55", "DeepCool", "Windows 10 Pro x64"))
    EVMs[5].setCase(210, 480, 440,"Miditower")
    EVMs[5].setCPU("Ryzen 5 1600", "PGA", 3.7, 6, True)
    EVMs[5].setMemory(16,"DIMM",4,1024,False,False)
    EVMs[5].setGPU("AMD Radeon RX560", 1800, 4, False)
    EVMs[5].setMotherboard("ASUS PRIME X-370", "AM4", "Realtek ALCS1220A 8-Channel", "Multi-VGA output: Display Port, HDMI", 8, False, False, "ATX")
    EVMs[5].setPSU("Chieftec 600W Proton", "80 PLUS Bronze", 600)
    EVMs[5].setCooling(3, "DeepCool Gammax 400")
    EVMs[5].printFullInformaton()

Main()