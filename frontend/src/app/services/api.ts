import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class ApiService {
  private api = '/api';  // proxy redirige a http://localhost:8000/api

  constructor(private http: HttpClient) {}

  getReservas(): Observable<any[]> {
    return this.http.get<any[]>(`${this.api}/reservas/`);
  }

  postReserva(data: any): Observable<any> {
    return this.http.post<any>(`${this.api}/reservas/`, data);
  }

  getClientes(): Observable<any[]> {
    return this.http.get<any[]>(`${this.api}/clientes/`);
  }

  postCliente(data: any): Observable<any> {
    return this.http.post<any>(`${this.api}/clientes/`, data);
  }
}