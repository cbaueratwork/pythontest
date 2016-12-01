# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import time
import random

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write('Hello, Universe!')


class TakeSomeTime(webapp2.RequestHandler):
  def get(self):
    wait_time = random.randint(100, 500);
    time.sleep(wait_time);
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write('Waited for ' + wait_time + 'ms before returning');


class PossibleException(webapp2.RequestHandler):
  def get(self):
    exception_seed = random.randint(0, 10)
    answer = 42 / exception_seed
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write('Divided 42 by ' + exception_seed + ', got ' + answer)



app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/time', TakeSomeTime),
  ('/divide', PossibleException),
], debug=True)


