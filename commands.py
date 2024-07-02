from time import strftime
date = strftime("%d%b%Y")
hour = strftime("%H")
minutes = strftime("%M")

if int(hour) < 17 and int(minutes) > 30:
  show = "matinee"
else:
  show = "evening"

class Hyperdeck:
  play = "play\n"
  stop = "stop\n"
  remote = "remote: enable: true\n"
  quit = "quit\n"

  def input(self, video, audio):
    return "configuration: video input: %s audio input: %s\n" %(video, audio)

  def record(self, hyperdeckNumber):
    return "record: name: %s %s hyperdeck%s \n" %(date, show, hyperdeckNumber)

class Multiview:
  soloEnable = "CONFIGURATION:\nSolo enabled: true\n\n"
  soloDisable = "CONFIGURATION:\nSolo enabled: false\n\n"
  def routeInput(self, input):
    input -= 1
    return "VIDEO OUTPUT ROUTING:\n16 %d\n\n" %(input)

class Smarthub:
  def routeInput(self, input, output):
    input -= 1
    output -= 1
    return "VIDEO OUTPUT ROUTING:\n%s %d\n\n" %(output, input)