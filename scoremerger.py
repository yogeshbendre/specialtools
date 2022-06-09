import argparse





def main():
    parser=argparse.ArgumentParser(description='Score Merger')
    parser.add_argument("-fw", "--folder", help="Folder path", required=True)
    parser.add_argument("-v", "--vc", help= "VC Name", required=True)
    parser.add_argument("-w", "--wcp", help= "WCP Cluster", required=True)

    args2 = parser.parse_args()
    args = vars(args2)
    wcp_cluster_name = args['wcpClusterName']
    wcp_namespace_prefix = args['wcpNsPrefix']

