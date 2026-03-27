import requests
import sys

def pull(robot_number):
    url = f"https://igniteinsights.org/analysis/team/{robot_number}/visualizations"
    print(requests.get(url).text)


def main():
    try:
        robot_number = sys.argv[1]
    except Exception:
        print("Invalid robot number given")
        return
    
    pull(robot_number)

if __name__=='__main__':
    main()