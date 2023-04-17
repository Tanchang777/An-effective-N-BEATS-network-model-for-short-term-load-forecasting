import numpy as np

NNC = list(range(1,31,))
print('len NNC',len(NNC))
print(NNC)
forecast_length = 15
A=2
B=forecast_length -1
avg=[]
# 当len（forecast）< forecast_length
if  forecast_length>A:
    for i in range(0,A+forecast_length-1):
        if i == 0:
            avg.append(NNC[i])
            pass

        elif 0<i<=A-1:
            N = np.mean(NNC[i:forecast_length * i + 1:B])
            avg.append(N)
            pass

        elif forecast_length-1>=i>A-1:
            avg.append(np.mean(NNC[i:forecast_length * i + 1:B]))
            pass

        elif A + forecast_length - 2 > i > forecast_length-1:
            j = i - forecast_length + 1
            avg.append(np.mean(NNC[i + B * j:len(NNC):B]))
            pass

        else:
            c = i - forecast_length+1
            avg.append(NNC[ i + c * B ])
            pass
    pass

    # 当len（forecast）= forecast_length
elif forecast_length == A:
    for i in range(0,A+forecast_length-1):
        if i == 0:
            avg.append(NNC[i])
            pass

        elif 0<i<=forecast_length-1:
            N = np.mean(NNC[i :forecast_length * i + 1 : B])
            avg.append(N)
            print('第一个elif',avg)
            pass

        elif A + forecast_length - 2 > i > forecast_length-1:
            j = i - forecast_length + 1
            avg.append(np.mean(NNC[i + B * j:len(NNC):B]))
            pass

        else:
            c = i - forecast_length+1
            avg.append(NNC[ i + c * B ])
            pass
        pass

    # 当len（forecast）> forecast_length
else:
    for i in range(0,A+forecast_length-1):
        if i == 0:
            avg.append(NNC[i])
            pass

        elif 0<i<=forecast_length-1:
            N = np.mean(NNC[i:forecast_length * i + 1:B])
            avg.append(N)
            print('-------------------------------',avg)
            pass
        # 问题出在这里
        elif A>i>forecast_length-1:
            t = i - forecast_length + 1
            avg.append(np.mean(NNC[i + B * t : len(NNC) - (A-i) * forecast_length + 1 : B]))
            print('A>i>forecast_length-1:',avg)
            pass

        # 在这里下端触底了
        elif A + forecast_length - 2 > i >= A-1:
            j = i - forecast_length + 1
            avg.append(np.mean(NNC[i + B * j:len(NNC) - 1 : B]))
            pass

        else:
            c = i - forecast_length+1
            avg.append(NNC[ i + c * B ])
            pass
        pass

print('avg',avg)
print(type(avg))
print('len(avg)',len(avg))