# === Stage 57: Add structured result objects for command handlers ===
# Project: SavingsGoal
class GoalResult:
    def __init__(self, status='ok', message='', data=None, error=None):
        self.status = status
        self.message = message
        self.data = data
        self.error = error

    def to_dict(self):
        if self.error is not None:
            return {'status': self.status, 'error': self.error}
        if self.data is not None:
            return {'status': self.status, 'data': self.data}
        return {'status': self.status, 'message': self.message}

    def to_json(self):
        return json.dumps(self.to_dict(), indent=2)


def success_result(data, message=None):
    return GoalResult(status='ok', message=message or 'Operation completed', data=data)


def error_result(message, code='error'):
    return GoalResult(status=code, message=message)


def empty_result(message='No data'):
    return GoalResult(status='ok', message=message)
