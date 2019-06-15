import pandas as pd
import sys


def main(fil):
	a = pd.read_csv(fil)
	a.columns= ["stock","date","time","open","high","low","close","x","y"]
	times=["09:06","09:08","15:31","15:32"]
	b = [k[1] for k in a.groupby(a['date'])]
	targetCols= ["stock","date","time","open","high","low","close"]
	final = pd.DataFrame(columns=targetCols)
	datelist = []
	for df in b:
		df = df[~df.time.isin(times)]
		dflist = [df[i:i+5] for i in range(0,len(df),5)]
		nf=pd.DataFrame()
		chunks=[]
		for e in dflist:
			first = e.iloc[0]
			last = e.iloc[-1]
			n = str(first['stock'])
			d = str(first['date'])
			t = str(last['time'])
			o = str(first['open'])
			h = str(max(e['high']))
			l = str(min(e['low']))
			c = str(last['close'])
			frame = [n,d,t,o,h,l,c]
			nf = pd.DataFrame([frame],columns=targetCols)
			chunks.append(nf)
		final=pd.concat(chunks,ignore_index=True)
		datelist.append(final)
	finalfinal = pd.concat(datelist,ignore_index=True)
	finalfinal.to_csv(r"C:\Users\GOPIKRISHNAN-LT\Downloads\NiftyDB\new.csv")

if __name__ == "__main__":
	fil=sys.argv[1]
	main(fil)