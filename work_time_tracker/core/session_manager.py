import pickle


class SessionManager:
    def __init__(self, filepath="sessions.pkl"):
        self.sessions = []
        self.filepath = filepath
        self.load_sessions()

    def add_session(self, session):
        self.sessions.append(session)
        self.save_sessions()

    def save_sessions(self):
        with open(self.filepath, "wb") as f:
            pickle.dump(self.sessions, f)

    def load_sessions(self):
        try:
            with open(self.filepath, "rb") as f:
                self.sessions = pickle.load(f)
        except (FileNotFoundError, EOFError):
            self.sessions = []

    def get_sessions_for_current_week(self, current_week):
        return [session for session in self.sessions if session.week == current_week]

    def get_sessions_for_current_day(self, current_day):
        return [session for session in self.sessions if session.day == current_day]
