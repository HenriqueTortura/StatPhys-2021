module Metropolis_for_2D_Ising

contains

	subroutine Metropolis(J, H, k_B, T, L, t_END, Energy, Magnetization)

		real (kind = 8), intent(in) :: J, H, k_B, T
		integer, intent(in) :: L, t_END
		
		real (kind = 8) :: Delta_H
		integer :: AllocateStatus, i, k
		
		integer, dimension(2) :: candidate
		integer, dimension(4) :: neighbors
		
		integer, dimension(:,:), allocatable :: spins
		
		real (kind = 8), dimension(t_END+1), intent(out) :: Energy, Magnetization
		
		! Definindo estado inicial
		allocate(spins(L,L), stat = AllocateStatus)
		if (AllocateStatus /= 0) stop '*** Not enough memory ***'
		spins = 1 !Define todos os spins como +1
		
		! Iniciando vetores de energia e magnetização
		Energy(1) = 0
		! Varre todos os sítios da rede
		do i=1, L
			do k=1, L
				! Obtém os vizinho de acordo com as condições periódicas de contorno
				neighbors = (/ spins(L*(1-merge(0,1,(i-1)==0))+(i-1), k),&
				&spins(mod(i,L)+1, k),&
				&spins(i, L*(1-merge(0,1,(k-1)==0))+(k-1)), &
				&spins(i, mod(k,L)+1) /)
				! Cálculo da energia
				Energy(1) = Energy(1) - spins(i,k)*(J*sum(neighbors)/2 + H)
			end do
		end do
		! Cálculo da magnetização
		Magnetization(1) = sum(spins)
		
		! Percorre pelos "passos temporais elementares"
		do i=1, t_END
			! Sorteio do sítio
			candidate = (/ Random_Integer(1,L), Random_Integer(1,L) /)
			! Avaliação dos vizinho de acordo com as condições periódicas de contorno
			neighbors = (/ spins(L*(1-merge(0,1,(candidate(1)-1)==0))+(candidate(1)-1),candidate(2)),&
					&spins(mod(candidate(1),L)+1,candidate(2)),&
					&spins(candidate(1),L*(1-merge(0,1,(candidate(2)-1)==0))+(candidate(2)-1)), &
					&spins(candidate(1),mod(candidate(2),L)+1) /)
					
			! Atualização de energia e magnetização (caso não venha a flipar)
			Energy(i+1) = Energy(i)
			Magnetization(i+1) = Magnetization(i)
			! Cálculo da variação energética
			Delta_H = 2 * spins(candidate(1),candidate(2)) * (J*sum(neighbors) + H)
			
			! Condição de flip
			if ( (Delta_H < 0) .or. (rand() <= exp(-Delta_H/(k_B*T))) ) then
				spins(candidate(1),candidate(2)) = -1*spins(candidate(1),candidate(2))
				! Atualização no caso de flipar
				Energy(i+1) = Energy(i) + Delta_H
				Magnetization(i+1) = Magnetization(i) + 2*spins(candidate(1),candidate(2))
			end if
		end do
		
	end subroutine Metropolis
	
	function Random_Integer(n,m)
		!integer :: n, m
		real (kind = 8) :: u
		
		call random_number(u)
		Random_Integer = n + FLOOR((m+1-n)*u)

	end function Random_Integer

end module Metropolis_for_2D_Ising
