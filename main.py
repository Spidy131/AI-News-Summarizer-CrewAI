from crew import news_crew

def main():
    print("=" * 50)
    print("🤖 AI News Summarizer")
    print("=" * 50)

    result = news_crew.kickoff()

    print("\n\n===== FINAL RESULT =====\n")
    print(result)

if __name__ == "__main__":
    main()