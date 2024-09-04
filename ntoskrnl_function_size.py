import ida_funcs
import idc

#The IDA Pro Python script to calculate the code size of the Windows kernel subsystems inside an IDB file
#Note that IDA Free doesn't have the capability to execute Python scripts

def main():
    prefixes = ['Ke', 'Ps', 'Se', 'Io', 'Ki', 'Cc', 'Mm', 'Mi', 'Ob', 'Cm', 'Ex', 'Hal', 'Po', 'Etw', 'Nt', 'Zw', 'Pi', 'Pnp', 'Ppm', 'Vf']
    size_dict = {prefix: 0 for prefix in prefixes}
    size_dict['Others'] = 0

    total_size = 0

    # Iterate over all functions by index
    for i in range(ida_funcs.get_func_qty()):
        func = ida_funcs.getn_func(i)
        if not func:
            continue
        
        func_name = idc.get_func_name(func.start_ea)
        func_size = func.end_ea - func.start_ea

        total_size += func_size
        matched = False
        for prefix in prefixes:
            if func_name.startswith(prefix):
                size_dict[prefix] += func_size
                matched = True
                break
        if not matched:
            size_dict['Others'] += func_size

    print("Function Size by Class:")
    print("=======================")
    for prefix in prefixes:
        size_kb = size_dict[prefix] / 1024  # Convert bytes to KB
        percentage = (size_dict[prefix] / total_size) * 100
        print(f"{prefix}: {size_kb:.2f} KB ({percentage:.2f}%)")
    
    others_kb = size_dict['Others'] / 1024
    others_percentage = (size_dict['Others'] / total_size) * 100
    print(f"Others: {others_kb:.2f} KB ({others_percentage:.2f}%)")

    total_size_kb = total_size / 1024
    print("=======================")
    print(f"Total size of all functions: {total_size_kb:.2f} KB")

if __name__ == "__main__":
    main()
