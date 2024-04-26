from datetime import datetime, timedelta
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QTimer

from ui.qt_main_window import Ui_MainWindow
from core.session import Session
from core.session_manager import SessionManager


class WorkTimerApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.current_datetime = datetime.now()
        self.current_week = self.current_datetime.isocalendar()[1]
        self.current_day = self.current_datetime.day

        self.session_manager = SessionManager()
        self.current_session = None

        self.startTimerButton.clicked.connect(self.toggle_session)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_ui)
        self.timer.start(1000)

        self.ui_update_timer = QTimer()
        self.ui_update_timer.timeout.connect(self.update_labels)
        self.ui_update_timer.start()

        self.update_ui()
        self.update_labels()

    def update_ui(self):
        self.current_datetime = datetime.now()
        self.currentDateTimeLabel.setText(
            self.current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        )
        self.check_day_and_week_transition()

    def check_day_and_week_transition(self):
        new_week = self.current_datetime.isocalendar()[1]
        new_day = self.current_datetime.day
        if new_week != self.current_week:
            self.current_week = new_week
        if new_day != self.current_day:
            self.current_day = new_day
            if self.current_session and self.current_session.running:
                self.end_session()
                self.start_session()

    def toggle_session(self):
        if self.current_session and self.current_session.running:
            self.end_session()
            self.startTimerButton.setText("Начать работу")
        else:
            self.start_session()
            self.startTimerButton.setText("Закончить работу")

    def start_session(self):
        self.current_session = Session()
        self.session_manager.add_session(self.current_session)

    def end_session(self):
        if self.current_session:
            self.current_session.end_session()
            self.session_manager.save_sessions()

    def update_labels(self):
        self.update_week_label()
        self.update_day_label()
        self.update_session_label()

    def update_week_label(self):
        total_week_time = sum(
            session.duration
            for session in self.session_manager.sessions
            if session.week == self.current_week
        )
        self.weeklyWorkTimeLabel.setText(
            f"Время за неделю: {self.format_time(total_week_time)}"
        )

    def update_day_label(self):
        total_day_time = sum(
            session.duration
            for session in self.session_manager.sessions
            if session.day == self.current_day
        )
        self.dailyWorkTimeLabel.setText(
            f"Время за день: {self.format_time(total_day_time)}"
        )

    def update_session_label(self):
        if self.current_session and self.current_session.running:
            current_session_time = self.current_session.duration
            self.currentWorkTimeLabel.setText(
                f"Время за сессию: {self.format_time(current_session_time)}"
            )
        else:
            self.currentWorkTimeLabel.setText("")

    def closeEvent(self, event):
        if self.current_session and self.current_session.running:
            self.end_session()
        event.accept()

    def format_time(self, seconds):
        return str(timedelta(seconds=int(seconds)))
