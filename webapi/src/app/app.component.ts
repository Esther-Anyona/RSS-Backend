import { Component, OnInit } from '@angular/core';
import { UsersService } from './users.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  register: any;

  constructor(private usersService:UsersService) {}

  ngOnInit(): void { 
      this.register = {
        username:'',
        email:'',
        password:'',
      };
  } 
  registerUser() {
    this.usersService.registerUser(this.register).subscribe(
      response => {
        alert('User' +this.register.username + 'has been created!')
      },
      error => console.log('error', error)
    );

  }
}
