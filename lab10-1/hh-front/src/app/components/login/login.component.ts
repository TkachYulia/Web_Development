import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  logged: boolean = false

  constructor(private userService: UserService) {}
  
  userModel = {
    username: '',
    password: ''
  }

  ngOnInit() {
    let token = localStorage.getItem('token')
    if(token) {
      this.logged = true
    }
  }

  onLogin() {
    this.userService.login(this.userModel).subscribe(
      res => {
         console.log(res)
        localStorage.setItem('token', res.token)
        this.logged = true
      }
    )
  }

  onLogout() {
    localStorage.clear()
    this.logged = false
  }
}
