# Michalis Gavriel / Giannis Loizou / Alexandros Pelekanos, for the purposes of SWitches project Summer 2025
import json
import os
"""
Reminder/Refresher/Information:
The following things found in the code are purely for annotation reasons
and helps the interpreter find any mistakes you did in your code

    varName:expectedVarType
    def functionName -> returnType

"""

'''
Extra class incase i get to using the RAW data Linpack generated.
TODO (extra, nice thing for later): Add __str__ definition for printing
'''
class RunDefs:
    def __init__(self, reps: int = 0, totalt: float = 0.0, dgefaperc: float = 0.0,
                 dgeslperc: float = 0.0, overheadperc: float = 0.0, kflops: float = 0.0) -> None:
        self.reps: int = reps
        self.time: float = totalt
        self.dgefapercentage: float = dgefaperc
        self.dgeslpercentage: float = dgeslperc
        self.overheadpercentage: float = overheadperc
        self.kflops: float = kflops

    # Compatible with JSON, pass obj.__dict__ to json.dumps()
    def __dict__(self) -> dict:
        return {"reps": self.reps,
                "time": self.time,
                "dgefapercentage": self.dgefapercentage,
                "dgeslpercentage": self.dgeslpercentage,
                "overheadpercentage": self.overheadpercentage,
                "kflops": self.kflops}

    # (Lazy) Convenience feature for compatibility
    def toJSON(self) -> str:
        return json.dumps(self.__dict__())

    # TODO: Decompress json strings into the class (for easier analysis later)
    # Decompress JSON string
    def importJSON(self, parsablejson:str) -> None:
        temp:dict = json.loads(parsablejson) # <= Currently only a dict with the meat
        pass


class LinSWSummary:

    def __init__(self) -> None:
        self.name:str = str()
        self.precision:str = str()
        self.warmupTimes:list[float] | list[RunDefs] = list()
        self.perfTimes:list[float] | list[RunDefs] = list()
        self.optType:str = 'mul'
        self.hwCores:int = 0
        self.hwThreads:int = 0
        self.allocatedThreads:int = 0

    def parsefile(self, filename:str) -> None:
        if not os.path.isfile(filename):
            raise IOError('File not found')


        with open(filename, 'r') as file: # Reminder: Handle ALL exceptions by the caller, not here
            # TODO: Separate filename from path to file (incase that's used)
            if not filename.startswith('linSW'):
                raise NameError('Improper file naming: expected "linSW" naming')


            # Left splitting
            temp = filename.split('_[')
            if len(temp) != 2:
                raise NameError('Improper file naming: bad square bracket(s) (\'[\')')
            self.name = temp[0]

            # Middle and right splitting
            temp = temp[1].split(']_')
            if len(temp) != 2:
                raise NameError('Improper file naming: bad square bracket(s) (\']\')')
            tempm:str = temp[0]
            tempr:str = temp[1]

            # Get precision
            self.precision = self.name.split('_')[1]
            if self.precision != 'dp' or self.precision != 'sp':
                raise NameError('Improper file naming: Bad precision naming')


            # Partitioning middle params of SWitches
            temp = tempm.split('_')
            if len(temp) != 3:
                raise NameError('Improper file naming: bad SWitches name formatting')

            # mul(ticore) / Hardware threads
            if not temp[0].startswith('mul'):
                raise NameError('Improper file naming: SWitches "mul" modifier not detected')
            self.hwCores = temp[0].split('mul')[1]
            if not self.hwCores.isnumeric():
                raise NameError('Improper file naming: bad "mul" parsing')

            # HW Threads
            if not temp[1].isnumeric():
                raise NameError('Improper file naming: bad Hardware thread parsing')
            self.hwThreads = temp[1]

            # Software (allocated) threads
            if not temp[0].startswith('t'):
                raise NameError('Improper file naming: SWitches "t" modifier not detected')
            self.swCores = temp[0].split('t')[1]
            if not self.hwCores.isnumeric():
                raise NameError('Improper file naming: bad software thread count parsing')



        pass
        # raise NotImplementedError

    # TODO: Helper function for parsing class to JSON
    def __dict__(self) -> dict:
        raise NotImplementedError

    # Lazy JSONify
    def toJSON(self) -> str:
        return json.dumps(self.__dict__())

    # TODO: Implement JSON string import to class
    def importJSON(self, parsablejson:str) -> None:
        temp:dict = json.loads(parsablejson) # <= Currently only a dict with the meat
        pass

# TODO: Make a non-SW version of the class (combining both into one was a disaster waiting to happen)


if __name__ == '__main__':
    target:str = input(f'Give filename of file to analyze (if file is not in same dir, use "{os.path.sep}" to the path): ')
    if not os.path.isfile(target):
        print('File not found.')
        exit(-1)


        pass
