import { Component, OnInit } from '@angular/core';
import { ApiService, Reserva } from '../../services/api';

@Component({
  selector: 'app-reserva-list',
  templateUrl: './reserva-list.html',
  styleUrls: ['./reserva-list.scss'],
})
export class ReservaListComponent implements OnInit {
  reservas: Reserva[] = [];

  constructor(private api: ApiService) {}

  ngOnInit() {
    this.api.getReservas().subscribe((data: Reserva[]) => {
      this.reservas = data;
    });
  }
}