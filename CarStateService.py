import rpyc

class LightsService(rpyc.Service):

    state = {
        "signal": "none",
        "headlights": "none",
        "breaklights": "none",
        "hazard": "none",
        "move": "none"
    }

    def exposed_get_state(self):
        return self.state;

    def exposed_signal(self, mode):
        self.state["signal"] = mode
        
    def exposed_move(self, mode):
        self.state["move"] = mode

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(LightsService(), port=18861)
    t.start()
