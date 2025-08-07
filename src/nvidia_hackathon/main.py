from nvidia_hackathon.crew import crew

from dotenv import load_dotenv
load_dotenv()


if __name__ == "__main__":
    result = crew.kickoff(inputs={"sector": "Healthcare AI"})
    print("\n\nFinal Investment Memo:\n")
    print(result)


# if __name__ == "__main__":
#     result = crew.kickoff(inputs={"team_name": "Corinthians"})
#     print(result)