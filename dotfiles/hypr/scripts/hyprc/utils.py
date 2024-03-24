import subprocess
import colorsys
import json
import sys

class Utils:

    @staticmethod
    def isDark(dark:str):
        try:
            if(dark == "true"): return True
            elif(dark != "true" and dark != "false"):
                print("insert bool value, [true] | [false]")
                sys.exit(1)
            else:
                return False
        except Exception as e:
            raise(e)
    
    @staticmethod
    def hex_to_hsl(hex_color:str):
        hex_color = hex_color.lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        rgb_normalized = tuple(component / 255.0 for component in rgb)
        hsl = colorsys.rgb_to_hls(*rgb_normalized)
        hsl = (hsl[0] * 360, hsl[1], hsl[2])

        return hsl


    def read_file(self, file_path: str):
        try:
            with open(file_path, "r") as f:
                return f.read()
        except Exception as e:
            print("Error to the read file", e)
            exit(1)

    def write_file(self, file_path: str, content:str):
        try:
            with open(file_path, "w") as f:
                f.write(content)
        except Exception as e:
            print("Error to the save file:", e)
            exit(1)


    def copy(self, fileC:str, fileDst:str):
        content = self.read_file(fileC)
        self.write_file(fileDst, content)


    def run_command(self,command: str):
        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            status_code = result.returncode

            output = result.stdout.strip()

            response_data = {"data": output, "code": str(status_code)}

            json_data = json.dumps(response_data)

            return json_data

        except subprocess.CalledProcessError as e:
            error_data = {"data": e.stderr.strip(), "code": str(e.returncode)}

            json_error = json.dumps(error_data)

            return json_error

    def reload_app(self,name,signal):
        try:
            self.run_command(f"pkill -{signal} {name}") 
            # subprocess.run(["pkill", f"-{signal}", name], check=True)
        except subprocess.CalledProcessError as e:
            raise(e)
            return False
        return True