class Member:
  club = "Judo"
  fee = 1200

  def Info(self):
    print(f"The name of the student is {self.name},the club is {self.club} and the fees is {self.fee}.")


Antra = Member()
Antra.name = "Antra"
Antra.Info()
# Member.Info(Antra)