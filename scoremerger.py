import argparse
import os


def mergeScores(f,vc,wcp):
    
    allFiles = os.listdir()
    myscores = {vc: {"avg":"0", wcp: {"avg":"0"}}}
    
    for s in myfiles:
        if('.csv' in s):
            mydata = ""
            with open(s,"r") as fp:
                mydata = fp.read().split("\n")[1:]
            for e in mydata:
                tkc = e.split(",")[0].replace("-kubeconfig","")
                score = e.split(",")[1]
                if tkc not in myscores.keys():
                    myscores[tkc] = {}
                myscores[vc][wcp][tkc][s.replace(".csv","")] = scor
    vcavg = 0
    wcpavg = 0
    wcptotal = 0
    wcpn = 0
    for t in myscores[vc][wcp].keys():
        if "avg" in t:
            continue:
        ttotal = 0
        tn = 0
        for sc in myscores[vc][wcp][t].keys():
            if "avg" in sc:
                continue
            ttotal = ttotal + int(myscores[vc][wcp][t][sc])
            tn = tn + 1
        
        tavg = 0
        if tn>0:
            tavg = ttotal/tn
        myscores[vc][wcp][t]["avg"] = str(tavg)
        wcptotal = wcptotal + tavg
        wcpn = wcp + 1
    
    if wcpn>0:
        wcpavg = wcptotal/wcpn
    myscores[vc][wcp]["avg"] = str(wcpavg)
    myscores[vc]["avg"] = str(wcpavg)
    print(myscores)
        
    




def main():
    parser=argparse.ArgumentParser(description='Score Merger')
    parser.add_argument("-fw", "--folder", help="Folder path", required=True)
    parser.add_argument("-v", "--vc", help= "VC Name", required=True)
    parser.add_argument("-w", "--wcp", help= "WCP Cluster", required=True)

    args2 = parser.parse_args()
    args = vars(args2)
    f = args['folder']
    vc = args['vc']
    wcp = args['wcp']
    
    mergeScores(f,vc,wcp)
    
    
    
    
    
if __name__ == "__main__":
    main()


